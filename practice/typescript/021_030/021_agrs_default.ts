{
    function showTime(time?: Date): string{
        if(time===undefined){
            return '現在時刻:' + (new Date()).toLocaleString();
        } else {
            return '現在時刻:' + time.toLocaleString();
        }
    }

    console.log(showTime());
}
