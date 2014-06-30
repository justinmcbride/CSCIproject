var DSP = "https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata";
var qString = "?app_name=TEST";

angular.module("sensingApp",["customFilters"])
	.controller('sensingCtrl', function($scope, $http){
    $http.get(DSP + qString).success(function(data) {
      $scope.data = data;
    });
});

