var delimiter = ';';

/*
function onOpen() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var csvMenuEntries = [{name: "Exportar Arquivo CSV", functionName: "saveAsCSV"}];
  ss.addMenu("Criar CSV Personalizado", csvMenuEntries);
};
*/

function saveAsCSV() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(); 
  var sheet = ss.getSheetByName('Dados');
  var folderName = ss.getName().toLowerCase().replace(/ /g,'_') + '_csv';
  var existsFolder = DriveApp.getFoldersByName(folderName);
  if (existsFolder.hasNext()) {
    folder = existsFolder.next();
  } else {
    folder = DriveApp.createFolder(folderName);
    folder.setSharing(DriveApp.Access.ANYONE, DriveApp.Permission.VIEW);
  }
  var fileName = 'dados_' + Utilities.formatDate(new Date(), "GMT-03:00", "dd-MM-yyyy_HH-mm-ss") + '.csv';
  var csvFile = convertRangeToCsvFile(fileName, sheet);
  var file = folder.createFile(fileName, csvFile);
  file.setSharing(DriveApp.Access.ANYONE, DriveApp.Permission.VIEW);
  var downloadURL = file.getDownloadUrl().slice(0, -8);
  showurl(downloadURL);
  
}

function showurl(downloadURL) {
   var link = HtmlService.createHtmlOutput('<center><a href="' + downloadURL + '">Clique AQUI com o botão direito e depois em "Abrir link em uma nova guia" para fazer o download</a><center>');
  SpreadsheetApp.getUi().showModalDialog(link, 'O arquivo CSV está pronto!');
}

function convertRangeToCsvFile(csvFileName, sheet) {
  try {
    var data = sheet.getDataRange().getDisplayValues();
    if (data.length > 1) {
      var rows = [];
      data.forEach(row => {
        var inserir = true;
        var cols = [];
        row.forEach(col => {
          if (col != "") 
            if (isNaN(col))
                cols.push(`"${col.toString().replace(/"/g, '""')}"`);
            else
                cols.push(col);
          else
            inserir = false
        });
        if (inserir)
          rows.push(cols.join(delimiter));
      });
      
      return rows.join('\r\n');
    }
  } catch(err) {
    Logger.log(err);
    Browser.msgBox(err);
  }
}

function redefinirPlanilha() {
  var ui = SpreadsheetApp.getUi();
  var response = ui.alert('Atenção', 'Todos os dados serão excluídos. Deseja Continuar?', ui.ButtonSet.YES_NO);

  // Process the user's response.
  if (response == ui.Button.YES) {
    var ss = SpreadsheetApp.getActiveSpreadsheet(); 
    var sheet = ss.getSheetByName('Disponibilidades');
    var range = sheet.getRangeList(['A5:K54']);
    range.clearContent();
    sheet = ss.getSheetByName('Dados');
    range = sheet.getRangeList(['A2:C51']);
    range.clearContent();
  } 
  
}
