Papa.parse("/countries.csv", {
  download: true,
  header: false,
  complete: function(results) {
    results.data.map((data, index)=> {
    let table = document.getElementById("tbl-data");
    generateTableHead(table, data);
    })
  }
})

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for(let key of data) {
    let th = document.createElement("th");
    let text  = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  };
}

function hyperlinker() {
  let tr = document.body.getElementsByTagName("tr")[2];
  let td = tr.getElementsByTagName("td");
  for(item in td)
    item.style.color = "red"

}
