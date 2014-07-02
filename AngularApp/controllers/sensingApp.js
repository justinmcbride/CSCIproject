var DSP = "https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata";
var qString = "?app_name=TEST&limit=100&order=_id%20desc";

angular.module("sensingApp",["customFilters","kendo.directives"])
	.controller('sensingCtrl', function($scope, $http){
    
    $http.get(DSP + qString).success(function(data) {
      $scope.data = data.record;
    });
  
  	// Custom variables within $scope.chart are used for manipulating kendo charts
  	$scope.chart = {
    dataSource: {
      data: $scope.data
    },
    title:"Temperature Recordings",
    seriesDefaults: {
      type: 'line',
      style: 'smooth',
      color:'blue'
    },
    series: [{
      field: 'sensorData.Temperature'
    }]
  };

  $scope.$watchCollection('data', function(newData) {
    $scope.chart.dataSource.data = newData;
  });
  
});

