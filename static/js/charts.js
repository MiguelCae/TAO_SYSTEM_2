var data = {{ json | safe}} 
var data2 = {{ json2 | safe}}
var data3 = {{ json3 | safe}}
// data[0]["fields"].ATTRIBUTE
var ctx = document.getElementById("myDoughnutChart");
var myDoughnutChart = new Chart(ctx, {
type: 'doughnut',
data: {
    labels:['Mascotas en adopcion','Mascotas en custodia', 'col3'],
    datasets:[{
        label: 'Num de datos',
        data: [data, data2, data3],
        backgroundColor:[
            "rgba(138,5,190,1)",
            "rgba(38,11,88,1)",
            "rgba(255, 233, 0)",

        ]

    }]
}

});

<canvas id="myDoughnutChart" width="100" height="100" >

</canvas>


    var data = {{ json | safe}} 
    var data2 = {{ json2 | safe}}
    var data3 = {{ json3 | safe}}
    // data[0]["fields"].ATTRIBUTE
    var ctx = document.getElementById("myDoughnutChart");
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels:['Mascotas en adopcion','Mascotas en custodia', 'col3'],
        datasets:[{
            label: 'Num de datos',
            data: [data, data2, data3],
            backgroundColor:[
                "rgba(138,5,190,1)",
                "rgba(38,11,88,1)",
                "rgba(255, 233, 0)",

            ]

        }]
    }

});
