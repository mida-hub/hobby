{
    class MyClassA{
        private data = 10;
    }

    class MyClassB{
        #data = 10;
    }

    let c1 = new MyClassA();
    console.log(c1['data']);
    let c2 = new MyClassB();
    console.log(c2['data']);
}
