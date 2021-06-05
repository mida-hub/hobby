import('../lib/App')
.then(app => {
    app.showMessage();
})

async function main(){
    let app = await import('../lib/App');
    app.showMessage();
}
