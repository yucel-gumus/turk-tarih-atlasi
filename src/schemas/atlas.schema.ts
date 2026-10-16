import { z } from 'zod';

export const RegionEnum = z.enum([
  'bozkir',
  'turkistan',
  'bati',
  'kuzey',
  'iran',
  'anadolu',
  'diger',
  'gunumuz',
]);
export type Region = z.infer<typeof RegionEnum>;

export const ConfidenceEnum = z.enum(['kayit', 'tartismali', 'rivayet']);
export type Confidence = z.infer<typeof ConfidenceEnum>;

export const BattleResultEnum = z.enum([
  'zafer',
  'yenilgi',
  'sonucsuz',
  'belirsiz',
  'antlasma',
]);
export type BattleResult = z.infer<typeof BattleResultEnum>;

export const CertaintyEnum = z.enum([
  'kesin',
  'olasi',
  'muhtemel',
  'tartismali',
  'rivayet',
]);
export type Certainty = z.infer<typeof CertaintyEnum>;

export const SourceSchema = z.object({
  title: z.string().trim().min(1),
  url: z.string().url().refine((value) => new URL(value).protocol === 'https:', 'Kaynak HTTPS olmalı'),
});
export type Source = z.infer<typeof SourceSchema>;

export const WarSchema = z.object({
  name: z.string(),
  when: z.string().optional().default(''),
  foe: z.string().optional().default(''),
  result: BattleResultEnum.optional().default('belirsiz'),
  note: z.string().optional().default(''),
});
export type War = z.infer<typeof WarSchema>;

export const PersonSchema = z.object({
  name: z.string(),
  mother: z.string().nullable().optional().transform((v) => v ?? ''),
  note: z.string().nullable().optional().transform((v) => v ?? ''),
  certainty: CertaintyEnum.optional().default('kesin'),
});
export type Person = z.infer<typeof PersonSchema>;

export const RulerSchema = z.object({
  id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
  name: z.string(),
  aliases: z.array(z.string()).optional().default([]),
  title: z.string().optional().default(''),
  birth: z.number().int().nullable().optional(),
  birthNote: z.string().optional().default(''),
  death: z.number().int().nullable().optional(),
  deathNote: z.string().optional().default(''),
  reign: z.tuple([z.number().int().nullable(), z.number().int().nullable()]),
  reignNote: z.string().optional().default(''),
  claim: z.boolean().optional().default(false),
  summary: z.string().optional().default(''),
  traits: z.array(z.string()).optional().default([]),
  contribution: z.string().optional().default(''),
  harm: z.string().optional().default(''),
  wives: z.array(PersonSchema).optional().default([]),
  children: z.array(PersonSchema).optional().default([]),
  familyNotes: z.array(z.string()).optional().default([]),
  wars: z.array(WarSchema).optional().default([]),
  legends: z.array(z.string()).optional().default([]),
  // Kaynak zorunlu: SCHEMA.md ve `npm run validate` her devlette ve her
  // hükümdarda en az bir kaynak şart koşar. Şema da aynı sözleşmeyi uygular ki
  // veri şemadan geçtiğinde kaynak eksikliği sessizce boş diziye düşmesin.
  sources: z.array(SourceSchema).min(1),
});
export type Ruler = z.infer<typeof RulerSchema>;

export const StateSchema = z.object({
  id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
  name: z.string(),
  short: z.string().optional(),
  aliases: z.array(z.string()).optional().default([]),
  region: RegionEnum,
  start: z.number().int(),
  end: z.number().int(),
  startNote: z.string().optional().default(''),
  endNote: z.string().optional().default(''),
  capital: z
    .union([z.string(), z.array(z.string())])
    .transform((v) => (Array.isArray(v) ? v.join(', ') : v))
    .optional()
    .default(''),
  religion: z.string().optional().default(''),
  confidence: ConfidenceEnum.optional().default('kayit'),
  confidenceNote: z.string().optional().default(''),
  summary: z.string().optional().default(''),
  legacy: z.string().optional().default(''),
  essay: z.array(z.string()).optional().default([]),
  // Kaynak zorunlu: SCHEMA.md ve `npm run validate` her devlette ve her
  // hükümdarda en az bir kaynak şart koşar. Şema da aynı sözleşmeyi uygular ki
  // veri şemadan geçtiğinde kaynak eksikliği sessizce boş diziye düşmesin.
  sources: z.array(SourceSchema).min(1),
  rulers: z.array(RulerSchema).optional().default([]),
});
export type State = z.infer<typeof StateSchema>;

/** Soy ağacı: her devletin tek bir üst düğümü ve o bağın türü vardır. */
export const EdgeKindEnum = z.enum(['devam', 'kol', 'miras']);
export type EdgeKind = z.infer<typeof EdgeKindEnum>;

export const LineageSchema = z.object({
  root: z.string(),
  contextNodes: z.array(
    z.object({
      id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
      name: z.string(),
      short: z.string(),
      start: z.number().int(),
      end: z.number().int(),
      summary: z.string().min(1),
      sources: z.array(SourceSchema).min(1),
    })
  ),
  edges: z.array(
    z.object({
      parent: z.string(),
      child: z.string(),
      kind: EdgeKindEnum,
      note: z.string().min(1),
    })
  ),
});
export type Lineage = z.infer<typeof LineageSchema>;
export type ContextNode = Lineage['contextNodes'][number];
