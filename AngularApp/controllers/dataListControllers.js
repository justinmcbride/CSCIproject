angular.module("sensingApp")
	.constant("dataListActiveClass", "btn-primary")
	.controller("dataListCtrl", function($scope, $filter, dataListActiveClass){

		var selectedData = null; 

		$scope.selectData = function(newInfo){
			selectedData = newInfo;
		}

		$scope.deviceFilterFn = function(record){
			return selectedData == null || record.boardName == selectedData;
		}

		$scope.getDeviceClass = function (boardName) {
			return selectedData == boardName ? dataListActiveClass : "";
		}
	});