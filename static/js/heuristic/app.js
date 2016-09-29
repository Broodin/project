$(window).on('load', function() {

		// dataPoints
		var dataPoints1 = [];

		var chart = new CanvasJS.Chart("chartContainer",{
			zoomEnabled: true,
			
			title: {
				text: "Elapsed time for applications"		
			},
			toolTip: {
				shared: true,
				content:"{x} : {y} sec"
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
				title:"elapsed time",
				includeZero: true,
				suffix:'s'
			}, 
			data: [{ 
				
				// dataSeries1			
				type: "column",
				xValueType: "dateTime",
				click:onClick,
				showInLegend: false,
				name: "",
				
				dataPoints:dataPoints1
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

		
		
		var init = function(){
				var time;
				var finish;
				var elapsed;
				var yValue1 = 65; 
				var job;

				// count is number of times loop runs to generate random dataPoints. 
				var result1 = $('#my-data').data().name;
				var result = $('#my-data').data().result;
				var x = result1.replace("[","").replace("]","").replace(/ /g,"").replace("(","").split("),(");
				//console.log(typeof result.toString());
				for(i=0;i<x.length;i++){
					//console.log(x[i]);
					var arr = x[i].split(",");
					//console.log(arr);
					time = new Date(parseInt(arr[1]));
					finish = new Date(parseInt(arr[2]));
					// add interval duration to time				
					elapsed = Math.abs(finish-time)/1000;
					job=arr[0].replace(/'/g,"");
					//console.log(time,elapsed);
					if(job==result.toString()){
					dataPoints1.push({
						x: time.getTime(),
						y: elapsed,
						z:job,
						color:'black'
					});

					}
					else{
				// pushing the new values
					dataPoints1.push({
						x: time.getTime(),
						y: elapsed,
						z:job,
						color:'#379EAD'
					});
					}

				
				}
			

			chart.render();

		
		};
		
		init();
		function onClick(e){
			var d =e.dataPoint.z

			window.location.assign("/"+d);
		}
		
		
		 
		
});








	