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
  const table = document.getElementById("tbl-data");
  const row = table.rows[2];
  const childrenArray = Array.from(row.children);

  childrenArray.forEach(child => {
    child.innerHTML = "<a href='" + child.innerHTML + "'>"+child.innerHTML + "</a>"
  });
}

