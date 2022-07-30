function append(tag, timestamp, record)
    new_record = record
    new_record["filterd_time"] = os.time()
    new_record["filterd_date"] = os.date()
    return 1, timestamp, new_record
end
