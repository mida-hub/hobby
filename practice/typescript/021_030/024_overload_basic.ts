{
    function show(value: number): void;
    function show(value: boolean): void;

    function show(value: any): void{
        if (typeof value === 'number'){
            console.log(value.toFixed(0));
        } else {
            console.log(value ? '真':'偽');
        }
    }

    show(10.358);
    show(false);
}
