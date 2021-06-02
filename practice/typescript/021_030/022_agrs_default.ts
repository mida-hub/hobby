{
    function showTime2(time: Date = new Date()): string{
        return '現在時刻:' + time.toLocaleString();
    }

    console.log(showTime2());
}
