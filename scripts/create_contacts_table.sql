create table if not exists public.contacts (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  phone text not null,
  active boolean not null default true,
  created_at timestamp with time zone default now()
);

create index if not exists idx_contacts_active on public.contacts (active);

alter table public.contacts enable row level security;

drop policy if exists "Allow read to anon" on public.contacts;

create policy "Allow read to anon"
  on public.contacts for select
  using (true);
