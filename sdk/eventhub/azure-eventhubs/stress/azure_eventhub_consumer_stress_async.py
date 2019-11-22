import time
import argparse
import asyncio
import os
import logging
from collections import defaultdict
from azure.eventhub.aio import EventHubConsumerClient
from azure.storage.blob.aio import ContainerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from logger import get_logger

parser = argparse.ArgumentParser()
parser.add_argument("--link_credit", default=3000, type=int)
parser.add_argument("--output_interval", type=float, default=1000)
parser.add_argument("--duration", help="Duration in seconds of the test", type=int, default=30)
parser.add_argument("--consumer", help="Consumer group name", default="$default")
parser.add_argument("--offset", help="Starting offset", default="-1")
parser.add_argument("--partitions", help="Number of partitions. 0 means to get partitions from eventhubs", type=int, default=0)
parser.add_argument("--load_balancing_interval", help="time duration in seconds between two load balance", type=float, default=10)
parser.add_argument("--conn_str", help="EventHub connection string",
                    default=os.environ.get('EVENT_HUB_PERF_32_CONN_STR'))
parser.add_argument("--eventhub", help="Name of EventHub")
parser.add_argument("--address", help="Address URI to the EventHub entity")
parser.add_argument("--sas_policy", help="Name of the shared access policy to authenticate with")
parser.add_argument("--sas_key", help="Shared access key")
parser.add_argument("--aad_client_id", help="AAD client id")
parser.add_argument("--aad_secret", help="AAD secret")
parser.add_argument("--aad_tenant_id", help="AAD tenant id")
parser.add_argument("--payload", help="payload size", type=int, default=1024)
parser.add_argument("--storage_conn_str", default=os.environ.get("AZURE_STORAGE_CONN_STR"))
parser.add_argument("--storage_container_name", default=os.environ.get("AZURE_STORAGE_CONTAINER"))
parser.add_argument("--print_console", help="print to console", type=bool, default=False)

args = parser.parse_args()
LOGGER = get_logger("stress_receive_async.log", "stress_receive_async", level=logging.INFO, print_console=args.print_console)
LOG_PER_COUNT = args.output_interval

start_time = time.perf_counter()
recv_cnt_map = defaultdict(int)
recv_time_map = dict()


async def on_event_received(partition_context, event):
    recv_cnt_map[partition_context.partition_id] += 1
    if recv_cnt_map[partition_context.partition_id] % LOG_PER_COUNT == 0:
        total_time_elapsed = time.perf_counter() - start_time

        partition_previous_time = recv_time_map.get(partition_context.partition_id)
        partition_current_time = time.perf_counter()
        recv_time_map[partition_context.partition_id] = partition_current_time
        LOGGER.info("Partition: %r, Total received: %r, Time elapsed: %r, Speed since start: %r/s, Current speed: %r/s",
                    partition_context.partition_id,
                    recv_cnt_map[partition_context.partition_id],
                    total_time_elapsed,
                    recv_cnt_map[partition_context.partition_id] / total_time_elapsed,
                    LOG_PER_COUNT / (partition_current_time - partition_previous_time) if partition_previous_time else None
                    )


async def run(args):
    class EventHubConsumerClientTest(EventHubConsumerClient):
        async def get_partition_ids(self):
            if args.partitions != 0:
                return [str(i) for i in range(args.partitions)]
            else:
                return await super(EventHubConsumerClientTest, self).get_partition_ids()

    checkpoint_store = BlobCheckpointStore(ContainerClient.from_connection_string(args.storage_conn_str, args.storage_container_name))
    client = EventHubConsumerClientTest.from_connection_string(
        args.conn_str, args.consumer, eventhub_name=args.eventhub, checkpoint_store=checkpoint_store,
        load_balancing_interval=args.load_balancing_interval
    )
    async with client:
        task = asyncio.ensure_future(client.receive(on_event_received, prefetch=args.link_credit))
        await asyncio.sleep(args.duration)
    await task


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(args))
