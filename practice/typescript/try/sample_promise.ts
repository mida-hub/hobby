{
    function a_non_sync(){
        return Promise.resolve(1);
    }

    function a_sync(){
        return 2;
    }

    function a_main(){
        console.log(a_non_sync());
        console.log(a_sync()+1);
        a_non_sync().then(value => console.log(value+1));
    }

    a_main();
}
