from apscheduler.schedulers.blocking import BlockingScheduler
import requests

schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=24)
def hourly_task():
    fetch_opentimes()


def fetch_opentimes():
    response = requests.get('https://bfgnet.de/sennelager-range-access')
    print("Fetching OpenTimes")

    if response.status_code != 200:
        print("could not fetch")
        return
    with open('opentimes/opentimes', 'w') as f:
        f.write(response.content.decode('utf-8'))


fetch_opentimes()
schedule.start()
