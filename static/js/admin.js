var chart;
$(function () {Highcharts.setOptions({
			global: {
				useUTC: false
			}
		});
    
        // Create the chart
        $('#container').highcharts('StockChart', {
			credits: {
				enabled: false
			},
			chart: {
				height: 400
			},

            rangeSelector: {
				inputPosition:{
					x:-40,
				},
                inputEnabled: true,
                selected: 0,
				inputDateFormat: '%d-%b-%Y %H:%M:%S',
				inputEditDateFormat: '%m-%d,%Y %H:%M:%S',
				inputBoxWidth: 140,
                buttons: [{
                    type: 'minute',
                    count: 30,
                    text: '30m'
                },{
                    type: 'minute',
                    count: 60,
                    text: '1h'
                }, {
                    type: 'day',
                    count: 1,
                    text: '1d'
                }, {
                    type: 'week',
                    count: 1,
                    text: '1w'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1m'
                }, {
                    type: 'year',
                    count: 1,
                    text: '1y'
                }, {
                    type: 'all',
                    text: 'All'
                }]
            },
			buttonSpacing: 100,
			navigator: {
				height: 30
			},

            title: {
                text: '<strong>Cluster Usage</strong>'
            },
			
			yAxis: {
                title: {
                    text: 'Percentage',
					style: {
						color: '#525151',
						font: '15px Helvetica',
						fontWeight: 'bold'
					},
                },
				opposite: false,
				
            },
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: {
					second: '%Y-%m-%d<br/>%H:%M:%S',
					minute: '%Y-%m-%d<br/>%H:%M',
					hour: '%d-%m-%Y<br/>%H:%M',
					day: '%Y<br/>%m-%d',
					week: '%Y<br/>%m-%d',
					month: '%Y-%m',
					year: '%Y'
				},
                title: {
                    text: 'Date',
					style: {
						color: '#525151',
						font: '15px Helvetica',
						fontWeight: 'bold'
					},
                },
            },
			exporting: {
            buttons: {
                customButton: {
                    x: 0,
					y:37,
                    onclick: function () {
                        var min = $('.highcharts-range-selector[name=min]').val();
						var max = $('.highcharts-range-selector[name=max]').val();
						min = new Date(min).getTime();
						max = new Date(max).getTime();
						
						//console.log(new Date(min).getTime(),new Date(max).getTime());
						$.ajax({
							type: 'POST',
							data: 'min='+min+'&max='+max,
							success: function() { window.location.href = "url?min="+min+"&max="+max; },
							error: function(){ alert("error") },
							url: '/url',
							cache:false
						});
						 
                    },
                    text:'Go'
                }
            }
			},
            series: [{
                name: 'cluster usage',
                data: (function(){
					var data = [];
					var res1 = $('#my-data').data();
					//console.log(res1);
					var x = res1.name.replace("[","").replace("]","").replace(/ /g,"").replace("(","").split("),(");
					
					//console.log(x[0],x.length);
					for(i=0;i<x.length;i++){
						//console.log(x[i]);
						var arr = x[i].split(",");
						var time = parseInt(arr[3]);
						date = new Date(time);
						value = parseFloat(arr[2]);
						//console.log(date,value);
						data.push([
							date.getTime(),
							
							value
						]);
					}
					return data;
				}())
            }]
		});
    });
	
$(document).ready(function() {
    var t= $('#example').DataTable( {
        "pagingType": "full_numbers",
		"columnDefs": [ {
            "searchable": false,
            "orderable": false,
            "targets": 0
        } ],
        "order": [[ 1, 'desc' ]]
    } );	
	
	 t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
} );
	
		
