$(window).on('load', function() {
		// dataPoints
		
		var dataPoints1 = [];
		var chart = new CanvasJS.Chart("chartContainer6",{
			zoomEnabled: true,
			height:300,
			width:1200,
			title: {
				text: "Mapper Time"		
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

				title:"Score",
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
					
			var result1 = $('#my-data').data().maptime;
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

			// updating legend text with  updated with y Value 
			//chart.options.data[0].legendText = " cluster " + yValue1 + "%";
			

			chart.render();

		};
		init1();
});
