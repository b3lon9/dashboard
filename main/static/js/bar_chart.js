$(function () {
    //const city = document.getElementById("city").value;
    const city_json = dict;
    
    var dataPoint_move = [];
    for (var i = 0; i < city_json.length; i++) {
        dataPoint_move.push({
            label: String(city_json[i].name),
            y: city_json[i].population
        });
    }
    
    
    
    var market_chart = new CanvasJS.Chart("market_chart", {
        animationEnabled: true,
        theme: "light1",
        exportEnabled:true,
        title:{
            text: "Volatility Index",
            fontSize:13,
        },
        axisY: {
            includeZero: true,
        },
        data: [
            {
                type: "column",
                indexLabelFontSize: 16,
                indexLabelPlacement:"outside",
                //데이터 넣는 곳
                dataPoints: dataPoint_move
                
            },
            

        ]
    });


        market_chart.render();
    console.log(dict)
    console.log(dataPoint_move)
});