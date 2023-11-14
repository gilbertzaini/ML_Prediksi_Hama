const { app, BrowserWindow, ipcMain } = require('electron');
const axios = require('axios');
const path = require('path');
const fs = require('fs');
const FormData = require('form-data');  // Add this line

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    mainWindow.loadFile('frontend/index.html');

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
    if (mainWindow === null) createWindow();
});

// Define a function to send the file to the Flask backend
const sendFileToFlask = async (filePath) => {
    try {
        const formData = new FormData();
        formData.append('file', fs.createReadStream(filePath));

        const response = await axios.post('http://localhost:5000/inference', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        console.log(response.data);
        // Handle the response as needed (update UI, display results, etc.)
    } catch (error) {
        console.error('Error sending file to Flask:', error);
    }
};

// Example: Send a file to Flask when a message is received from the renderer process
ipcMain.on('file-upload', (event, filePath) => {
    sendFileToFlask(filePath);
});
