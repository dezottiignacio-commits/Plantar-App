"""Actualiza la web de Plantar (Netlify) desde el catálogo de la App Clientes.
Uso: python3 tools/actualizar.py CATALOGO_APP.json CUITS.json [CARPETA_FOTOS_BAJADAS]
- Copia cuits.json.
- Mete en f/<id>.jpg las fotos bajadas (cualquier formato, achicadas a 900 px).
- Escribe catalogo.json sin fotos que no estén en f/ y lista (JSON) los ids de fotos que faltan.
"""
import json,sys,os,glob,shutil
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));F=os.path.join(R,'f');os.makedirs(F,exist_ok=True)
cat=json.load(open(sys.argv[1]))
shutil.copy(sys.argv[2],os.path.join(R,'cuits.json'))
if len(sys.argv)>3:
  for src in glob.glob(os.path.join(sys.argv[3],'*')):
    aid=os.path.splitext(os.path.basename(src))[0]
    if len(aid)!=32:continue
    dst=os.path.join(F,aid+'.jpg')
    try:
      from PIL import Image
      im=Image.open(src);im=im.convert('RGB') if im.mode!='RGB' else im
      if not aid in ('269d49ed3f7efb984ef8f5a2ccdffb15',) and max(im.size)>900 and im.size[0]<4000:im.thumbnail((900,900))
      im.save(dst,'JPEG',quality=85)
    except Exception:
      shutil.copy(src,dst)
falt=set()
for p in cat.get('productos',[]):
  if p.get('i') and not os.path.exists(os.path.join(F,p['i']+'.jpg')):falt.add(p['i']);del p['i']
  if p.get('sp') and not os.path.exists(os.path.join(F,p['sp'][0]+'.jpg')):falt.add(p['sp'][0]);del p['sp']
json.dump(cat,open(os.path.join(R,'catalogo.json'),'w'),ensure_ascii=False,separators=(',',':'))
print(json.dumps({'productos':len(cat.get('productos',[])),'faltan':sorted(falt)}))
