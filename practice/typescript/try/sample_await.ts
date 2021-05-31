{
    function b_non_sync(){
        return Promise.resolve(1);
    }

    async function b_main(){
        console.log(b_non_sync());
        console.log(await b_non_sync());
    }

    b_main()
}
