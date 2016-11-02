app

    .factory('cajaIngresoService', function($resource) {
    var url = 'http://localhost:8000/api/caja/';
    return {
        Caja: $resource(url + 'cajas/:id/', { id: '@id' }, {
            'update': { method: 'PUT' },

        }),
    };
});

// planillaService.Empleado.save(...);
// 'list': { method: 'GET' },