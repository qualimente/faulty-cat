import signal

from gremlins import faults, metafaults, triggers, tc

clear_network_faults = faults.clear_network_faults()
introduce_packet_loss = faults.introduce_network_packet_loss()
introduce_partition = faults.introduce_network_partition()
introduce_latency = faults.introduce_network_latency()
introduce_packet_reordering = faults.introduce_packet_reordering()

server_cmd = "nc.*4242"
nc_kill = faults.kill_processes([server_cmd], signal.SIGKILL)
nc_pause = faults.pause_processes([server_cmd], 5)

profile = [
    triggers.OneShot(clear_network_faults),
    # triggers.Periodic(
        # 10, metafaults.pick_fault([
        #     # kill -9s
        #     # (5, nc_kill),
        #     # pauses (simulate GC)
        #     (10, nc_pause),
        # ])),
    triggers.Periodic(
        10, metafaults.pick_fault([
            (10, clear_network_faults),
            # (10, introduce_packet_loss),
            (10, introduce_partition),
            (10, introduce_latency),
            # (10, introduce_packet_reordering),
        ])),
    #  triggers.WebServerTrigger(12321)
]

