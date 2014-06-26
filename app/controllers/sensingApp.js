var DSP = "https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata";
var qString = "?app_name=TEST&fielbs=*";

angular.module("sensingApp")
	.controller('sensingCtrl', function($scope, $http){
    $http.get(DSP + qString).success(function(data) {
      $scope.data = data;
    });
});

