var DSP = "https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata";
var qString = "?app_name=TEST&limit=15";

angular.module("sensingApp",["customFilters","kendo.directives"])
	.controller('sensingCtrl', function($scope, $http){
    
    $http.get(DSP + qString).success(function(data) {
      $scope.data = data.record;
    });
  
  	$scope.chart = {
    dataSource: {
      data: $scope.data
    },
    title:"Temperature Recordings",
    series: [{
      field: 'sensorData.Temperature'
    }],
    seriesDefaults: {
      type: 'area',
      style: 'smooth'
    }
  };

  $scope.$watchCollection('data', function(newData) {
    $scope.chart.dataSource.data = newData;
  });
  
});

