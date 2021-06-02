{
    let Counter = function(this: any) {
        this.count = 0;
    
        setInterval(()=>{this.count++;}, 1000);
    };
}
