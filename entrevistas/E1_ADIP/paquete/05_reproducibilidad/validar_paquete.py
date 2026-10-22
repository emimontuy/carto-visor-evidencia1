from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((root/p).read_text())
norm=lambda s:' '.join(s.split())
pages=(root/'01_fuente/e1_adip_transcripcion_extraida.txt').read_text().split('\f')
codes=read('02_codificacion/libro_de_codigos.json')
corpus=read('02_codificacion/corpus_codificado.json')
findings=read('03_analisis/hallazgos.json')
stories=read('04_desarrollo/historias_de_usuario.json')
bp=read('04_desarrollo/blueprint.json')
ids=lambda rows:{r['id'] for r in rows}
for rows in [codes,corpus,findings,stories,bp['requisitos']]: assert len(ids(rows))==len(rows),'ID duplicado'
for s in corpus:
 assert norm(s['fragmento_literal']) in norm(' '.join(pages[s['pagina']-1:s['pagina_fin']])),s['id']
 assert set(s['codigos'])<=ids(codes),s['id']
for c in codes: assert c['ejemplo_segmento'] in ids(corpus),c['id']
for f in findings:
 assert set(f['segmentos'])<=ids(corpus),f['id']
 assert set(f['codigos'])<=ids(codes),f['id']
for s in stories:
 assert set(s['segmentos'])<=ids(corpus),s['id']
 assert set(s['hallazgos'])<=ids(findings),s['id']
 assert set(s['requisitos'])<=ids(bp['requisitos']),s['id']
 assert s['criterios_aceptacion'],s['id']
for r in bp['requisitos']: assert set(r['historias'])<=ids(stories),r['id']
for o in read('06_fdo/objetos.json'):
 m=read(o['metadatos'])
 assert (root/o['archivo']).is_file()
 assert hashlib.sha256((root/o['archivo']).read_bytes()).hexdigest()==m['sha256'],o['clave']
 assert m['identificador_persistente_resoluble'] is None and m['pid_status']=='pendiente_de_registro'
 if o['esquema']:
  schema=read(o['esquema']); data=read(o['archivo'])
  try:
   import jsonschema
   jsonschema.Draft202012Validator(schema).validate(data)
  except ImportError:
   rows=data if isinstance(data,list) else [data]
   req=schema['items']['required'] if isinstance(data,list) else schema['required']
   for row in rows: assert set(req)<=set(row),'Campo obligatorio ausente'
manifest=root/'MANIFEST.sha256'
if manifest.exists():
 for line in manifest.read_text().splitlines():
  expected,rel=line.split('  ',1)
  assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==expected,rel
print(f'OK: {len(codes)} códigos, {len(corpus)} fragmentos, {len(findings)} hallazgos, {len(stories)} historias y {len(bp["requisitos"])} requisitos. Integridad y trazabilidad verificadas. Revisión humana pendiente.')
