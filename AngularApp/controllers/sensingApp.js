// Main app controller for 'sensingApp', with 'custom.filter' and 'kendo.directives'
// Defined variables include dreamfactory API, and required concatenation
var DSP = "https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata";
var qString = "?app_name=RemoteSensing&limit=10&order=_id%20desc";


angular.module("sensingApp",["customFilters","kendo.directives"])
  
  // Controller to define data for the $scope, after a get request to dreamfactory defined api
	.controller('sensingCtrl', function($scope, $http){
    
    // Get request to retrieving data and defining $scope.data
    $http.get(DSP + qString).success(function(data) {
      $scope.data = data.record;
    });
  
    // Custom variables within $scope.chart are used for manipulating kendo charts
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

  // watchCollection is required for the kendo charts
  $scope.$watchCollection('data', function(newData) {
    $scope.chart.dataSource.data = newData;
  });
  
});

