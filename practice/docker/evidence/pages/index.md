```trip_list
SELECT date(trip_start_timestamp) AS trip_start_date, fare FROM `bq-practice-329807.chicago_taxi_trips.taxi_trips` LIMIT 100
```

<DataTable
  data={trip_list}
/>

<LineChart
    data={trip_list}
    x='trip_start_date'
    y='fare'
    title='daily fare'
/>
