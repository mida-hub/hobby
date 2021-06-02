{
    function process(value: string | number){
        if (typeof value==='string'){
            return value.toUpperCase();
        }else{
            return value.toFixed(1);
        }
    }

    console.log(process(9.11));
    console.log(process('abc'));
}
