
// ---------------------- fetch API -------------------
console.log("runing..")
const myname = "salman khan "
const myage = 56


async function postData(url, data) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
function adddata(){
    console.log(myname)
    postData('api', {myname, myage})
        .then(data => {
        console.log(data);
        })
        .catch(error => {
        console.error(error);
        });
}
  
  // ---------------------- fetch API -------------------
  
