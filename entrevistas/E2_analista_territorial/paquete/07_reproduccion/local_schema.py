"""Validate the type, object and array keywords used by the local E2 schemas."""

def validate_local_schema(value, schema, path='$'):
    supported={'$schema','title','type','properties','required','additionalProperties','items'}
    unknown=set(schema)-supported
    if unknown:
        raise ValueError(f'{path}: palabras de esquema no soportadas {sorted(unknown)}')
    kind=schema.get('type')
    correct={
        'object':isinstance(value,dict),
        'array':isinstance(value,list),
        'string':isinstance(value,str),
        'integer':type(value) is int,
        'boolean':type(value) is bool,
        'null':value is None,
    }
    if kind is not None and not correct.get(kind,False):
        raise ValueError(f'{path}: se esperaba {kind}, se recibió {type(value).__name__}')
    if kind=='object':
        missing=set(schema.get('required',[]))-set(value)
        if missing: raise ValueError(f'{path}: campos requeridos ausentes {sorted(missing)}')
        properties=schema.get('properties',{})
        if schema.get('additionalProperties') is False:
            extra=set(value)-set(properties)
            if extra: raise ValueError(f'{path}: campos adicionales {sorted(extra)}')
        for key,child_schema in properties.items():
            if key in value: validate_local_schema(value[key],child_schema,path+'.'+key)
    elif kind=='array' and 'items' in schema:
        for index,item in enumerate(value):
            validate_local_schema(item,schema['items'],path+f'[{index}]')
