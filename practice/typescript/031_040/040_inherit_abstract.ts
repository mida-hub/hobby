{
    class Figure {
        constructor(protected width: number, protected height: number) {
        }
        getArea(): number{
            return 0;
        }
    }

    class Triangle extends Figure {
        getArea(): number{
            return this.width * this.height / 2;
        }
    }

    let t = new Triangle(10, 5);
    console.log(t.getArea());
}
