import pytest
import app.models as models
import datetime

@pytest.fixture
def calendar_events():
	d1=datetime.date(2020, 2, 1)
	d2=datetime.date(2020, 2, 1)
	e1=models.Event('event 1', d1, d2, 'location 1')

	d1=datetime.date(2019, 12, 1)
	d2=datetime.date(2020, 3, 2)   
	e2=models.Event('event 2', d1, d2, 'location 2')

	d1=datetime.date(2019,12,2)
	d2=datetime.date(2020,3,2)   
	e3=models.Event('event 2', d1, d2, 'location 2')

	d1=datetime.datetime(2020,2,1,8,10,0)
	d2=datetime.datetime(2020,2,1,9,10,0)
	e4=models.Event('event 1', d1, d2, 'location 1')

	d1=datetime.datetime(2020,2,3,8,10,0)
	d2=datetime.datetime(2020,2,3,9,10,0)
	e5=models.Event('event 1', d1, d2, 'location 1')

	events = [e1,e2,e3]
	events_without_time = [e4,e5]

	return events, events_without_time