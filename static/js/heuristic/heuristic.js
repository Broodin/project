function heuristic(name,result1,yaxis_name,div_id){
$(window).on('load', function() {
		// dataPoints
		
		var dataPoints1 = [];
		var chart = new CanvasJS.Chart(div_id,{
			zoomEnabled: true,
			height:300,
			width:1200,
			title: {
				text: name		
			},
			toolTip: {
				shared: true,
				content: "score <strong>{x}</strong> is <strong>{y}</strong>",
			},
			legend: {
				verticalAlign: "top",
				horizontalAlign: "center",
                                fontSize: 14,
				fontWeight: "bold",
				fontFamily: "calibri",
				fontColor: "black"
			},
			axisX: {
				title: "time",
				valueFormatString: "DD-MMM HH:mm"
			},
			axisY:{
				stripLines: [
				{
					value : null,
					label: "Average: "
				}
				],
				title:yaxis_name,
				minimum:0,
				suffix: '',
				includeZero: true
			}, 
			data: [{ 
				// dataSeries1
				type: "column",
				xValueType: "dateTime",
				showInLegend: true,
				name: "",
				dataPoints: dataPoints1
			}],
          legend:{
            cursor:"pointer",
            itemclick : function(e) {
              if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                e.dataSeries.visible = false;
              }
              else {
                e.dataSeries.visible = true;
              }
            }
          }
		});


 
		
		
	

		var init1 = function () {
			var time;
			var app;
			var score;
					
				//var result1 = $('#my-data').data().mapskew;
				var result = $('#my-data').data().result;
				var x = result1.replace("[","").replace("]","").replace(/ /g,"").replace("(","").split("),(");
				//console.log(typeof result.toString());
				//console.log(x);
				for(i=0;i<x.length;i++){
					var arr = x[i].split(",");
					time = new Date(parseInt(arr[3]));
					score = parseFloat(arr[1]);
					// add interval duration to time				
					job=arr[2].replace(/'/g,"");
					//console.log(job,result)
					if(job==result.toString()){
					dataPoints1.push({
						x: time.getTime(),
						y: score,
						z:job,
						color:'black'
					});

					}
					else{
				// pushing the new values
					dataPoints1.push({
						x: time.getTime(),
						y: score,
						z:job,
						color:'#379EAD'
					});
					}
				}
				var sum = 0;
				var length = chart.options.data[0].dataPoints.length;
				for( var i = 0; i < length; i++ )
					sum += chart.options.data[0].dataPoints[i].y;
				average = sum / length;
				console.log(chart.options.axisY);

				chart.options.axisY.stripLines[0].value = average;
				//chart.options.axisY.stripLines[0].label += average.toPrecision(3);

			// updating legend text with  updated with y Value 
			//chart.options.data[0].legendText = " cluster " + yValue1 + "%";
			

			chart.render();

		};
		init1();
});
}