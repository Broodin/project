	window.onload = function () {

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

		var time;
		var finish;
		var elapsed;
		var yValue1 = 65; 
		var job;
		
		var init = function(){

				// count is number of times loop runs to generate random dataPoints. 
				var rv = $('#my-data').data().name;
				var x = rv.replace("[","").replace("]","").replace(/ /g,"").replace("(","").split("),(");
				//console.log();
				
				for(i=0;i<x.length;i++){
					//console.log(i,x[i]);
					x[i] = x[i].replace(")","");
					var arr = x[i].split(",");
					time = new Date(parseInt(arr[5]));
					finish = new Date(parseInt(arr[6]));
				// add interval duration to time				
					elapsed = Math.abs(finish-time)/1000;
					job=arr[0];
				
				
				// pushing the new values
					dataPoints1.push({
						x: time.getTime(),
						y: elapsed,
						z:job
					});


				}
			

			chart.render();

		
		};
		
		init();
		function onClick(e){
			var d =e.dataPoint.z
			console.log(d);
			//window.location.assign("/"+d)
		}
		
		
		 
		
	}
	
$(document).ready(function() {
    var t= $('#example').DataTable( {
        "pagingType": "full_numbers",
		"columnDefs": [ {
            "searchable": false,
            "orderable": false,
            "targets": 0
        } ],
        "order": [[ 1, 'asc' ]]
    } );	
	
	 t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
} );	