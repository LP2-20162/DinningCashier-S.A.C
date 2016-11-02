app

    .controller('CajaCtr', function($scope, $window, cajaIngresoService) {

    $scope.cajaingreso = {};
    $scope.lista = [];

    $scope.listar = function() {
        cajaIngresoService.Caja.query().$promise.then(function(r) {
            $scope.lista = r;
        }, function(err) {
            console.log("Hay error");
        });
    };
    $scope.listar();

    $scope.sel = function(d) {
        //$scope.empleado = d;

        cajaIngresoService.Caja.get({ id: d.id }).$promise.then(function(r) {
            $scope.caja = r;
        }, function(err) {
            console.log("Hay error");
        });

    };

    $scope.save = function() {

        if ($scope.caja.id) {
            cajaIngresoService.Caja.update({ id: $scope.caja.id }, $scope.caja).$promise.then(function(r) {
                console.log("Editó " + r);

                $scope.listar();

            }, function(err) {
                console.log("Hay error");
            });

        } else {
            cajaIngresoService.Caja.save($scope.caja).$promise.then(function(r) {
                console.log("Insertó " + r);

                $scope.listar();

            }, function(err) {
                console.log("Hay error");
            });
        }


    };

    $scope.delete = function(d) {
        if ($window.confirm("Está seguro?")) {
            cajaIngresoService.Caja.delete({ id: d.id }).$promise.then(function(r) {
                console.log("Eliminado " + r);

                $scope.listar();

            }, function(err) {
                console.log("Hay error");
            });
        };
    };


});
