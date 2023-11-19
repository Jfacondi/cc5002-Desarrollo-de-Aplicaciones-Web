Highcharts.chart('container', {
  chart: {
    type: 'pie',
    backgroundColor: 'transparent',
    plotBorderWidth: null,
    plotShadow: false
    
  },
  title: {
      text: 'Hinchas',
      style: {
        color: 'white',
        fontSize: '24px',
      }
  },
  plotOptions: {
    pie: {
      colors: [
        '#B0E0E6', '#FFEEE0', '#FAC8C8', '#FDE2A7', '#D4F3C5',
        '#FFD6C4', '#FFC0CB', '#E6E6FA', '#FFDAB9', '#F0FFF0',
        '#FFFACD', '#ADD8E6', '#E0FFFF', '#F5F5DC', '#FFA07A',
        '#F0F8FF', '#FFF0F5', '#FAFAD2', '#E0FFFF', '#FFC3A0'
      ],
      dataLabels: {
          enabled: true,
          format: '{point.name}: {point.percentage:.1f}%'
      }
  }
  },
  series: [{
      name: 'Hinchas',
      data: []
  }]
});
Highcharts.chart('container2', {
    chart: {
      type: 'pie',
      backgroundColor: 'transparent',
      plotBorderWidth: null,
      plotShadow: false
      
    },
    title: {
        text: 'Artesanos',
        style: {
          color: 'white',
          fontSize: '24px',
      }
    },
    plotOptions: {
      pie: {
                   colors: [
                    '#B0E0E6', '#FFEEE0', '#FAC8C8', '#FDE2A7', '#D4F3C5',
                    '#FFD6C4', '#FFC0CB', '#E6E6FA', '#FFDAB9', '#F0FFF0',
                    '#FFFACD', '#ADD8E6', '#E0FFFF', '#F5F5DC', '#FFA07A',
                    '#F0F8FF', '#FFF0F5', '#FAFAD2', '#E0FFFF', '#FFC3A0'
                    ],
        dataLabels: {
            enabled: true,
            format: '{point.name}: {point.percentage:.1f}%'
        }
    }
    },
    series: [{
        name: 'Artesanos',
        data: []
    }]
});
fetch("http://localhost:3006/get_estadisticas")
  .then((response) => response.json())
  .then((hinchas) => {
    let parsedData = hinchas.hinchas.map((hincha) => {
      return [hincha.tipo, hincha.cantidad];
    });
    let parsedData2 = hinchas.artesanos.map((artesano) => {
        return [artesano.tipo, artesano.cantidad];
      });
  
    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );
    const chart2 = Highcharts.charts.find(
        (chart) => chart && chart.renderTo.id === "container2"
      );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
    chart2.update({
        series: [
          {
            data: parsedData2,
          },
        ],
      });
  })
  .catch((error) => console.error("Error:", error));

  function toggle1() {
    var x = document.getElementById("container");
    var y = document.getElementById("container2");
    var z = document.getElementById("btn1");
    if (x.style.display === "none") {
      z.value = "Ver Artesanos";
      x.style.display = "block";
      y.style.display = "none";
    } else {
      z.value = "Ver Hinchas"
      x.style.display = "none";
      y.style.display = "block";
    }
  }