// Controller for manipulating data bindings in app.html
angular.module("sensingApp")
	.constant("dataListActiveClass", "btn-primary")
	.controller("dataListCtrl", function($scope, $filter, dataListActiveClass){

		var selectedData = null; 

		// method for defining selectedData variable
		$scope.selectData = function(newInfo){
			selectedData = newInfo;
		}

		// method for activating filter after selectedData definition
		$scope.deviceFilterFn = function(record){
			return selectedData == null || record.boardName == selectedData;
		}

		// method for changing btn styling after selectedData definition
		$scope.getDeviceClass = function (boardName) {
			return selectedData == boardName ? dataListActiveClass : "";
		}
	});