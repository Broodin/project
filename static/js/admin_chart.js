window.onload = function (res1) {

		// dataPoints
		var dataPoints1 = [];
		var apps = [];

		var chart = new CanvasJS.Chart("chartContainer",{
			zoomEnabled: true,
			title: {
				text: "Cluster usage"		
			},
			toolTip: {
				shared: true,
				content: "Cluster usage on <strong>{x}</strong> is <strong>{y}</strong> %",
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
				valueFormatString: "YYYY-MMM-DD HH:mm"
			},
			axisY:{
				interval:20,
				maximum:100,
				title:"percentage",
				suffix: '%',
				includeZero: true
			}, 
			data: [{ 
				// dataSeries1
				color: "#80bfff",
				type: "column",
				xValueType: "dateTime",
				click:onClick,
				showInLegend: true,
				name: "cluster",
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
              chart.render();
            }
          }
		});



		var updateInterval = 300000;
		// initial value
		var yValue1 = 65; 
		
		var time;
		var app;
		
		// starting at 9.30 am

		var updateChart = function (count) {
				// count is number of times loop runs to generate random dataPoints. 
		
			{%for t in res1%}
				
				time = new Date("{{t[5]}}");
				// add interval duration to time				
				


				// generating random values
				var deltaY1 = .5 + Math.random() *(-.5-.5);
				

				// adding random value and rounding it to two digits. 
				yValue1 = Math.round((yValue1 + deltaY1)*100)/100;
				app = "{{t[0]}}"

				
				// pushing the new values
				dataPoints1.push({
					x: time.getTime(),
					y: yValue1,
					z: app
				});


			{%endfor%}

			// updating legend text with  updated with y Value 
			chart.options.data[0].legendText = " cluster " + yValue1 + "%";
			

			chart.render();

		};
		
		

		// generates first set of dataPoints 
		updateChart(3000);	
		 
		// update chart after specified interval 
		setInterval(function(){updateChart()}, updateInterval);
		
		function onClick(e){
			var d =e.dataPoint.x/1000;

			window.location.assign("/admin/"+d)
		}
	}	
