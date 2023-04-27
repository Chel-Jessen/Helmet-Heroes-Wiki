var urls = ["http://hhr-wiki.cheljessen.net/updateData", "https://helmet-heroes-reborn-bot.dakmj32dsalcx.repl.co/api/updateData"];

function sendAllSheetsAsJSON() {
  // send spreadsheet as JSON to server
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = spreadsheet.getSheets();
  var data = {};
  for (var i = 0; i < sheets.length; i++) {
    var sheet = sheets[i];
    var name = sheet.getName();
    var rows = sheet.getDataRange().getValues();
    data[name] = rows;
  }
  var json = JSON.stringify(data);
  var params = {
    method: "post",
    payload: json,
    headers: {
      "Content-Type": "application/json"
    },
    muteHttpExceptions: true
  };
  for(var i = 0; i < urls.length; i++){
    console.log(urls[i])
    var response = UrlFetchApp.fetch(urls[i], params);
    console.log(response)
  }
}



function createTimeDrivenTrigger() {
  ScriptApp.newTrigger('sendAllSheetsAsJSON')
      .timeBased()
      .everyMinutes(60)
      .create();
}