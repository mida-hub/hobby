{
    interface Car {
        type: string;
        run(): void;
    }

    let c: Car = {
        type: 'トラック',
        run() {
            console.log(`${this.type}が走ります。`);
        }
    };

    c.run();
}
