{
    interface Product{
        name: string;
        price: number;
    }

    function getProp2<T, K extends keyof T>(obj: T, name: K){
        return obj[name];
    }

    let p = {name: 'お弁当', price: 500};
    console.log(getProp2(p, 'name'));
    console.log(getProp2(p, 'price'));
}
