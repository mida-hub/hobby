{
    class Book {
        isbn: string;
        constructor(isbn: string) {
            this.isbn = isbn
          }
    }

    class Magazine {
        mcode: string;
    }

    function isBook(inf: Book | Magazine): inf is Book {
        return (inf as Book).isbn != undefined;
    }

    function getInfo(){
        let book = new Book('abc');
        return book;
    }

    let info = getInfo();
    if (isBook(info)){
        console.log(info.isbn);
    }
}
