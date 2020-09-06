let cnvs;
let main;
let fileInput;
let status;
let hndlr;
let data;
let trainButton;
let showDataButton;

function setup() {
    main = createDiv()

    cnvs = createCanvas(0, 0);
    fileInput = createFileInput(handleFile);
    trainButton = createButton("Train");
    trainButton.mousePressed(trainButtonClicked);
    trainButton.style("visibility","hidden")
    hndlr = new modelHandler;
}

function handleFile(file){
    print(file);
    try {
        let dataArr = CSVToArray(file.data,"\t");
        createTable(dataArr);
        data = hndlr.createDataListFromArray(dataArr,true);
        console.log(data);
        data.pop();
        trainButton.style("visibility","visible")
    } catch (error) {
        data = undefined;
        trainButton.style("visibility","hidden")
        console.error(error);
    }
}

function trainButtonClicked(){
    hndlr.train(data);
}

function createTable(tableData) {
    var table = document.createElement('table');
    var tableBody = document.createElement('tbody');
  
    tableData.forEach(function(rowData) {
      var row = document.createElement('tr');
  
      rowData.forEach(function(cellData) {
        var cell = document.createElement('td');
        cell.appendChild(document.createTextNode(cellData));
        row.appendChild(cell);
      });
  
      tableBody.appendChild(row);
    });
  
    table.appendChild(tableBody);
    document.body.appendChild(table);
  }