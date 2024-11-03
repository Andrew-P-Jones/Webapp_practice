async function loadPlot() {
    const response = await fetch('/get_plot');
    const data = await response.text();
    document.getElementById('plot-container').innerHTML = data;
}

async function loadTable() {
    const response = await fetch('/get_table_data');
    const data = await response.json();
    
    // Generate table HTML
    let tableHTML = "<table border='1'><tr>";
    
    // Set the order of teh columns
    const columnOrder = ['timestamp', 'high_low_diff', 'adjusted close', 'high', 'low'];

    // Add table headers in specified order
    columnOrder.forEach(col => {
        tableHTML += `<th>${col}</th>`;
        });
        tableHTML += "</tr>";
        
    // Add rows in specified column order
    data.forEach(row => {
        tableHTML += "<tr>";
        columnOrder.forEach(col => {
            tableHTML += `<td>${row[col]}</td>`; // Follows specified order for each cell
        });
        tableHTML += "</tr>";
    });
    
    tableHTML += "</table>";
    
    // Insert table HTML into container
    document.getElementById('table-container').innerHTML = tableHTML;
}

async function loadQuestion1() {
    const response = await fetch('/get_monthly_avg');
    const data = await response.text();
    document.getElementById('question1-container').innerHTML = data;
}

async function loadQuestion2() {
    const response = await fetch('/get_high_low_diff');
    const data = await response.text();
    document.getElementById('question2-container').innerHTML = data;
}

async function loadQuestion3Min() {
    const response = await fetch('/greatest_month_change/min');
    const data = await response.text();
    document.getElementById('question3min-container').innerHTML = data;
}

async function loadQuestion3Max() {
    const response = await fetch('/greatest_month_change/max');
    const data = await response.text();
    document.getElementById('question3max-container').innerHTML = data;
}
