async function loadPlot() {
    const response = await fetch('/get_plot');
    const data = await response.text();
    document.getElementById('plot-container').innerHTML = data.plot_html;
}