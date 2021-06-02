{
    function hoge(): never{
        throw new Error('Error is occured.');
    }

    function eternal(): never{
        while(true){
            console.log('loop');
        }
    }
}
