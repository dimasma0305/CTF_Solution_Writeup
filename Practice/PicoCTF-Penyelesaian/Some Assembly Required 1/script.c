/* Automically generated by wasm2c */
#include <math.h>
#include <string.h>

#include "script.h"
#define UNLIKELY(x) __builtin_expect(!!(x), 0)
#define LIKELY(x) __builtin_expect(!!(x), 1)

#define TRAP(x) (wasm_rt_trap(WASM_RT_TRAP_##x), 0)

#define FUNC_PROLOGUE                                            \
  if (++wasm_rt_call_stack_depth > WASM_RT_MAX_CALL_STACK_DEPTH) \
    TRAP(EXHAUSTION)

#define FUNC_EPILOGUE --wasm_rt_call_stack_depth

#define UNREACHABLE TRAP(UNREACHABLE)

#define CALL_INDIRECT(table, t, ft, x, ...)          \
  (LIKELY((x) < table.size && table.data[x].func &&  \
          table.data[x].func_type == func_types[ft]) \
       ? ((t)table.data[x].func)(__VA_ARGS__)        \
       : TRAP(CALL_INDIRECT))

#if WASM_RT_MEMCHECK_SIGNAL_HANDLER
#define MEMCHECK(mem, a, t)
#else
#define MEMCHECK(mem, a, t)  \
  if (UNLIKELY((a) + sizeof(t) > mem->size)) TRAP(OOB)
#endif

#if WABT_BIG_ENDIAN
static inline void load_data(void *dest, const void *src, size_t n) {
  size_t i = 0;
  u8 *dest_chars = dest;
  memcpy(dest, src, n);
  for (i = 0; i < (n>>1); i++) {
    u8 cursor = dest_chars[i];
    dest_chars[i] = dest_chars[n - i - 1];
    dest_chars[n - i - 1] = cursor;
  }
}
#define LOAD_DATA(m, o, i, s) load_data(&(m.data[m.size - o - s]), i, s)
#define DEFINE_LOAD(name, t1, t2, t3)                                                 \
  static inline t3 name(wasm_rt_memory_t* mem, u64 addr) {                            \
    MEMCHECK(mem, addr, t1);                                                          \
    t1 result;                                                                        \
    __builtin_memcpy(&result, &mem->data[mem->size - addr - sizeof(t1)], sizeof(t1)); \
    return (t3)(t2)result;                                                            \
  }

#define DEFINE_STORE(name, t1, t2)                                                     \
  static inline void name(wasm_rt_memory_t* mem, u64 addr, t2 value) {                 \
    MEMCHECK(mem, addr, t1);                                                           \
    t1 wrapped = (t1)value;                                                            \
    __builtin_memcpy(&mem->data[mem->size - addr - sizeof(t1)], &wrapped, sizeof(t1)); \
  }
#else
static inline void load_data(void *dest, const void *src, size_t n) {
  memcpy(dest, src, n);
}
#define LOAD_DATA(m, o, i, s) load_data(&(m.data[o]), i, s)
#define DEFINE_LOAD(name, t1, t2, t3)                        \
  static inline t3 name(wasm_rt_memory_t* mem, u64 addr) {   \
    MEMCHECK(mem, addr, t1);                                 \
    t1 result;                                               \
    __builtin_memcpy(&result, &mem->data[addr], sizeof(t1)); \
    return (t3)(t2)result;                                   \
  }

#define DEFINE_STORE(name, t1, t2)                                     \
  static inline void name(wasm_rt_memory_t* mem, u64 addr, t2 value) { \
    MEMCHECK(mem, addr, t1);                                           \
    t1 wrapped = (t1)value;                                            \
    __builtin_memcpy(&mem->data[addr], &wrapped, sizeof(t1));          \
  }
#endif

DEFINE_LOAD(i32_load, u32, u32, u32);
DEFINE_LOAD(i64_load, u64, u64, u64);
DEFINE_LOAD(f32_load, f32, f32, f32);
DEFINE_LOAD(f64_load, f64, f64, f64);
DEFINE_LOAD(i32_load8_s, s8, s32, u32);
DEFINE_LOAD(i64_load8_s, s8, s64, u64);
DEFINE_LOAD(i32_load8_u, u8, u32, u32);
DEFINE_LOAD(i64_load8_u, u8, u64, u64);
DEFINE_LOAD(i32_load16_s, s16, s32, u32);
DEFINE_LOAD(i64_load16_s, s16, s64, u64);
DEFINE_LOAD(i32_load16_u, u16, u32, u32);
DEFINE_LOAD(i64_load16_u, u16, u64, u64);
DEFINE_LOAD(i64_load32_s, s32, s64, u64);
DEFINE_LOAD(i64_load32_u, u32, u64, u64);
DEFINE_STORE(i32_store, u32, u32);
DEFINE_STORE(i64_store, u64, u64);
DEFINE_STORE(f32_store, f32, f32);
DEFINE_STORE(f64_store, f64, f64);
DEFINE_STORE(i32_store8, u8, u32);
DEFINE_STORE(i32_store16, u16, u32);
DEFINE_STORE(i64_store8, u8, u64);
DEFINE_STORE(i64_store16, u16, u64);
DEFINE_STORE(i64_store32, u32, u64);

#define I32_CLZ(x) ((x) ? __builtin_clz(x) : 32)
#define I64_CLZ(x) ((x) ? __builtin_clzll(x) : 64)
#define I32_CTZ(x) ((x) ? __builtin_ctz(x) : 32)
#define I64_CTZ(x) ((x) ? __builtin_ctzll(x) : 64)
#define I32_POPCNT(x) (__builtin_popcount(x))
#define I64_POPCNT(x) (__builtin_popcountll(x))

#define DIV_S(ut, min, x, y)                                 \
   ((UNLIKELY((y) == 0)) ?                TRAP(DIV_BY_ZERO)  \
  : (UNLIKELY((x) == min && (y) == -1)) ? TRAP(INT_OVERFLOW) \
  : (ut)((x) / (y)))

#define REM_S(ut, min, x, y)                                \
   ((UNLIKELY((y) == 0)) ?                TRAP(DIV_BY_ZERO) \
  : (UNLIKELY((x) == min && (y) == -1)) ? 0                 \
  : (ut)((x) % (y)))

#define I32_DIV_S(x, y) DIV_S(u32, INT32_MIN, (s32)x, (s32)y)
#define I64_DIV_S(x, y) DIV_S(u64, INT64_MIN, (s64)x, (s64)y)
#define I32_REM_S(x, y) REM_S(u32, INT32_MIN, (s32)x, (s32)y)
#define I64_REM_S(x, y) REM_S(u64, INT64_MIN, (s64)x, (s64)y)

#define DIVREM_U(op, x, y) \
  ((UNLIKELY((y) == 0)) ? TRAP(DIV_BY_ZERO) : ((x) op (y)))

#define DIV_U(x, y) DIVREM_U(/, x, y)
#define REM_U(x, y) DIVREM_U(%, x, y)

#define ROTL(x, y, mask) \
  (((x) << ((y) & (mask))) | ((x) >> (((mask) - (y) + 1) & (mask))))
#define ROTR(x, y, mask) \
  (((x) >> ((y) & (mask))) | ((x) << (((mask) - (y) + 1) & (mask))))

#define I32_ROTL(x, y) ROTL(x, y, 31)
#define I64_ROTL(x, y) ROTL(x, y, 63)
#define I32_ROTR(x, y) ROTR(x, y, 31)
#define I64_ROTR(x, y) ROTR(x, y, 63)

#define FMIN(x, y)                                          \
   ((UNLIKELY((x) != (x))) ? NAN                            \
  : (UNLIKELY((y) != (y))) ? NAN                            \
  : (UNLIKELY((x) == 0 && (y) == 0)) ? (signbit(x) ? x : y) \
  : (x < y) ? x : y)

#define FMAX(x, y)                                          \
   ((UNLIKELY((x) != (x))) ? NAN                            \
  : (UNLIKELY((y) != (y))) ? NAN                            \
  : (UNLIKELY((x) == 0 && (y) == 0)) ? (signbit(x) ? y : x) \
  : (x > y) ? x : y)

#define TRUNC_S(ut, st, ft, min, minop, max, x)                             \
  ((UNLIKELY((x) != (x)))                        ? TRAP(INVALID_CONVERSION) \
   : (UNLIKELY(!((x)minop(min) && (x) < (max)))) ? TRAP(INT_OVERFLOW)       \
                                                 : (ut)(st)(x))

#define I32_TRUNC_S_F32(x) TRUNC_S(u32, s32, f32, (f32)INT32_MIN, >=, 2147483648.f, x)
#define I64_TRUNC_S_F32(x) TRUNC_S(u64, s64, f32, (f32)INT64_MIN, >=, (f32)INT64_MAX, x)
#define I32_TRUNC_S_F64(x) TRUNC_S(u32, s32, f64, -2147483649., >, 2147483648., x)
#define I64_TRUNC_S_F64(x) TRUNC_S(u64, s64, f64, (f64)INT64_MIN, >=, (f64)INT64_MAX, x)

#define TRUNC_U(ut, ft, max, x)                                            \
  ((UNLIKELY((x) != (x)))                       ? TRAP(INVALID_CONVERSION) \
   : (UNLIKELY(!((x) > (ft)-1 && (x) < (max)))) ? TRAP(INT_OVERFLOW)       \
                                                : (ut)(x))

#define I32_TRUNC_U_F32(x) TRUNC_U(u32, f32, 4294967296.f, x)
#define I64_TRUNC_U_F32(x) TRUNC_U(u64, f32, (f32)UINT64_MAX, x)
#define I32_TRUNC_U_F64(x) TRUNC_U(u32, f64, 4294967296.,  x)
#define I64_TRUNC_U_F64(x) TRUNC_U(u64, f64, (f64)UINT64_MAX, x)

#define DEFINE_REINTERPRET(name, t1, t2)  \
  static inline t2 name(t1 x) {           \
    t2 result;                            \
    memcpy(&result, &x, sizeof(result));  \
    return result;                        \
  }

DEFINE_REINTERPRET(f32_reinterpret_i32, u32, f32)
DEFINE_REINTERPRET(i32_reinterpret_f32, f32, u32)
DEFINE_REINTERPRET(f64_reinterpret_i64, u64, f64)
DEFINE_REINTERPRET(i64_reinterpret_f64, f64, u64)


static u32 func_types[4];

static void init_func_types(void) {
  func_types[0] = wasm_rt_register_func_type(0, 0);
  func_types[1] = wasm_rt_register_func_type(2, 1, WASM_RT_I32, WASM_RT_I32, WASM_RT_I32);
  func_types[2] = wasm_rt_register_func_type(0, 1, WASM_RT_I32);
  func_types[3] = wasm_rt_register_func_type(2, 0, WASM_RT_I32, WASM_RT_I32);
}

static void w2c___wasm_call_ctors(void);
static u32 w2c_strcmp(u32, u32);
static u32 w2c_check_flag(void);
static void w2c_copy_char(u32, u32);

static u32 w2c_g0;
static u32 w2c_input;
static u32 w2c___dso_handle;
static u32 w2c___data_end;
static u32 w2c___global_base;
static u32 w2c___heap_base;
static u32 w2c___memory_base;
static u32 w2c___table_base;

static void init_globals(void) {
  w2c_g0 = 66864u;
  w2c_input = 1072u;
  w2c___dso_handle = 1024u;
  w2c___data_end = 1328u;
  w2c___global_base = 1024u;
  w2c___heap_base = 66864u;
  w2c___memory_base = 0u;
  w2c___table_base = 1u;
}

static wasm_rt_memory_t w2c_memory;

static wasm_rt_table_t w2c_T0;

static void w2c___wasm_call_ctors(void) {
  FUNC_PROLOGUE;
  FUNC_EPILOGUE;
}

static u32 w2c_strcmp(u32 w2c_p0, u32 w2c_p1) {
  u32 w2c_l2 = 0, w2c_l3 = 0, w2c_l4 = 0, w2c_l5 = 0, w2c_l6 = 0, w2c_l7 = 0, w2c_l8 = 0, w2c_l9 = 0, 
      w2c_l10 = 0, w2c_l11 = 0, w2c_l12 = 0, w2c_l13 = 0, w2c_l14 = 0, w2c_l15 = 0, w2c_l16 = 0, w2c_l17 = 0, 
      w2c_l18 = 0, w2c_l19 = 0, w2c_l20 = 0, w2c_l21 = 0, w2c_l22 = 0, w2c_l23 = 0, w2c_l24 = 0, w2c_l25 = 0, 
      w2c_l26 = 0, w2c_l27 = 0, w2c_l28 = 0, w2c_l29 = 0, w2c_l30 = 0, w2c_l31 = 0, w2c_l32 = 0, w2c_l33 = 0, 
      w2c_l34 = 0, w2c_l35 = 0, w2c_l36 = 0, w2c_l37 = 0, w2c_l38 = 0, w2c_l39 = 0, w2c_l40 = 0, w2c_l41 = 0, 
      w2c_l42 = 0, w2c_l43 = 0;
  FUNC_PROLOGUE;
  u32 w2c_i0, w2c_i1;
  w2c_i0 = w2c_g0;
  w2c_l2 = w2c_i0;
  w2c_i0 = 32u;
  w2c_l3 = w2c_i0;
  w2c_i0 = w2c_l2;
  w2c_i1 = w2c_l3;
  w2c_i0 -= w2c_i1;
  w2c_l4 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_p0;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 24, w2c_i1);
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_p1;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 20, w2c_i1);
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 24u);
  w2c_l5 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_l5;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 16, w2c_i1);
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 20u);
  w2c_l6 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_l6;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 12, w2c_i1);
  w2c_L1: 
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 16u);
    w2c_l7 = w2c_i0;
    w2c_i0 = 1u;
    w2c_l8 = w2c_i0;
    w2c_i0 = w2c_l7;
    w2c_i1 = w2c_l8;
    w2c_i0 += w2c_i1;
    w2c_l9 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i1 = w2c_l9;
    i32_store((&w2c_memory), (u64)(w2c_i0) + 16, w2c_i1);
    w2c_i0 = w2c_l7;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0));
    w2c_l10 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i1 = w2c_l10;
    i32_store8((&w2c_memory), (u64)(w2c_i0) + 11, w2c_i1);
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 12u);
    w2c_l11 = w2c_i0;
    w2c_i0 = 1u;
    w2c_l12 = w2c_i0;
    w2c_i0 = w2c_l11;
    w2c_i1 = w2c_l12;
    w2c_i0 += w2c_i1;
    w2c_l13 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i1 = w2c_l13;
    i32_store((&w2c_memory), (u64)(w2c_i0) + 12, w2c_i1);
    w2c_i0 = w2c_l11;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0));
    w2c_l14 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i1 = w2c_l14;
    i32_store8((&w2c_memory), (u64)(w2c_i0) + 10, w2c_i1);
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 11u);
    w2c_l15 = w2c_i0;
    w2c_i0 = 255u;
    w2c_l16 = w2c_i0;
    w2c_i0 = w2c_l15;
    w2c_i1 = w2c_l16;
    w2c_i0 &= w2c_i1;
    w2c_l17 = w2c_i0;
    w2c_i0 = w2c_l17;
    if (w2c_i0) {goto w2c_B2;}
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 11u);
    w2c_l18 = w2c_i0;
    w2c_i0 = 255u;
    w2c_l19 = w2c_i0;
    w2c_i0 = w2c_l18;
    w2c_i1 = w2c_l19;
    w2c_i0 &= w2c_i1;
    w2c_l20 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 10u);
    w2c_l21 = w2c_i0;
    w2c_i0 = 255u;
    w2c_l22 = w2c_i0;
    w2c_i0 = w2c_l21;
    w2c_i1 = w2c_l22;
    w2c_i0 &= w2c_i1;
    w2c_l23 = w2c_i0;
    w2c_i0 = w2c_l20;
    w2c_i1 = w2c_l23;
    w2c_i0 -= w2c_i1;
    w2c_l24 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i1 = w2c_l24;
    i32_store((&w2c_memory), (u64)(w2c_i0) + 28, w2c_i1);
    goto w2c_B0;
    w2c_B2:;
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 11u);
    w2c_l25 = w2c_i0;
    w2c_i0 = 255u;
    w2c_l26 = w2c_i0;
    w2c_i0 = w2c_l25;
    w2c_i1 = w2c_l26;
    w2c_i0 &= w2c_i1;
    w2c_l27 = w2c_i0;
    w2c_i0 = w2c_l4;
    w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 10u);
    w2c_l28 = w2c_i0;
    w2c_i0 = 255u;
    w2c_l29 = w2c_i0;
    w2c_i0 = w2c_l28;
    w2c_i1 = w2c_l29;
    w2c_i0 &= w2c_i1;
    w2c_l30 = w2c_i0;
    w2c_i0 = w2c_l27;
    w2c_l31 = w2c_i0;
    w2c_i0 = w2c_l30;
    w2c_l32 = w2c_i0;
    w2c_i0 = w2c_l31;
    w2c_i1 = w2c_l32;
    w2c_i0 = w2c_i0 == w2c_i1;
    w2c_l33 = w2c_i0;
    w2c_i0 = 1u;
    w2c_l34 = w2c_i0;
    w2c_i0 = w2c_l33;
    w2c_i1 = w2c_l34;
    w2c_i0 &= w2c_i1;
    w2c_l35 = w2c_i0;
    w2c_i0 = w2c_l35;
    if (w2c_i0) {goto w2c_L1;}
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 11u);
  w2c_l36 = w2c_i0;
  w2c_i0 = 255u;
  w2c_l37 = w2c_i0;
  w2c_i0 = w2c_l36;
  w2c_i1 = w2c_l37;
  w2c_i0 &= w2c_i1;
  w2c_l38 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load8_u((&w2c_memory), (u64)(w2c_i0) + 10u);
  w2c_l39 = w2c_i0;
  w2c_i0 = 255u;
  w2c_l40 = w2c_i0;
  w2c_i0 = w2c_l39;
  w2c_i1 = w2c_l40;
  w2c_i0 &= w2c_i1;
  w2c_l41 = w2c_i0;
  w2c_i0 = w2c_l38;
  w2c_i1 = w2c_l41;
  w2c_i0 -= w2c_i1;
  w2c_l42 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_l42;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 28, w2c_i1);
  w2c_B0:;
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 28u);
  w2c_l43 = w2c_i0;
  w2c_i0 = w2c_l43;
  goto w2c_Bfunc;
  w2c_Bfunc:;
  FUNC_EPILOGUE;
  return w2c_i0;
}

static u32 w2c_check_flag(void) {
  u32 w2c_l0 = 0, w2c_l1 = 0, w2c_l2 = 0, w2c_l3 = 0, w2c_l4 = 0, w2c_l5 = 0, w2c_l6 = 0, w2c_l7 = 0, 
      w2c_l8 = 0, w2c_l9 = 0, w2c_l10 = 0;
  FUNC_PROLOGUE;
  u32 w2c_i0, w2c_i1;
  w2c_i0 = 0u;
  w2c_l0 = w2c_i0;
  w2c_i0 = 1072u;
  w2c_l1 = w2c_i0;
  w2c_i0 = 1024u;
  w2c_l2 = w2c_i0;
  w2c_i0 = w2c_l2;
  w2c_i1 = w2c_l1;
  w2c_i0 = w2c_strcmp(w2c_i0, w2c_i1);
  w2c_l3 = w2c_i0;
  w2c_i0 = w2c_l3;
  w2c_l4 = w2c_i0;
  w2c_i0 = w2c_l0;
  w2c_l5 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_l5;
  w2c_i0 = w2c_i0 != w2c_i1;
  w2c_l6 = w2c_i0;
  w2c_i0 = 4294967295u;
  w2c_l7 = w2c_i0;
  w2c_i0 = w2c_l6;
  w2c_i1 = w2c_l7;
  w2c_i0 ^= w2c_i1;
  w2c_l8 = w2c_i0;
  w2c_i0 = 1u;
  w2c_l9 = w2c_i0;
  w2c_i0 = w2c_l8;
  w2c_i1 = w2c_l9;
  w2c_i0 &= w2c_i1;
  w2c_l10 = w2c_i0;
  w2c_i0 = w2c_l10;
  goto w2c_Bfunc;
  w2c_Bfunc:;
  FUNC_EPILOGUE;
  return w2c_i0;
}

static void w2c_copy_char(u32 w2c_p0, u32 w2c_p1) {
  u32 w2c_l2 = 0, w2c_l3 = 0, w2c_l4 = 0, w2c_l5 = 0, w2c_l6 = 0;
  FUNC_PROLOGUE;
  u32 w2c_i0, w2c_i1;
  w2c_i0 = w2c_g0;
  w2c_l2 = w2c_i0;
  w2c_i0 = 16u;
  w2c_l3 = w2c_i0;
  w2c_i0 = w2c_l2;
  w2c_i1 = w2c_l3;
  w2c_i0 -= w2c_i1;
  w2c_l4 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_p0;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 12, w2c_i1);
  w2c_i0 = w2c_l4;
  w2c_i1 = w2c_p1;
  i32_store((&w2c_memory), (u64)(w2c_i0) + 8, w2c_i1);
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 12u);
  w2c_l5 = w2c_i0;
  w2c_i0 = w2c_l4;
  w2c_i0 = i32_load((&w2c_memory), (u64)(w2c_i0) + 8u);
  w2c_l6 = w2c_i0;
  w2c_i0 = w2c_l6;
  w2c_i1 = w2c_l5;
  i32_store8((&w2c_memory), (u64)(w2c_i0) + 1072, w2c_i1);
  goto w2c_Bfunc;
  w2c_Bfunc:;
  FUNC_EPILOGUE;
}

static const u8 data_segment_data_0[] = {
  0x70, 0x69, 0x63, 0x6f, 0x43, 0x54, 0x46, 0x7b, 0x38, 0x38, 0x35, 0x37, 
  0x34, 0x36, 0x32, 0x66, 0x39, 0x65, 0x33, 0x30, 0x66, 0x61, 0x61, 0x65, 
  0x34, 0x64, 0x30, 0x33, 0x37, 0x65, 0x35, 0x65, 0x32, 0x35, 0x66, 0x65, 
  0x65, 0x31, 0x63, 0x65, 0x7d, 0x00, 0x00, 
};

static void init_memory(void) {
  wasm_rt_allocate_memory((&w2c_memory), 2, 65536);
  LOAD_DATA(w2c_memory, 1024u, data_segment_data_0, 43);
}

static void init_table(void) {
  uint32_t offset;
  wasm_rt_allocate_table((&w2c_T0), 1, 1);
}

/* export: 'memory' */
wasm_rt_memory_t (*WASM_RT_ADD_PREFIX(Z_memory));
/* export: '__wasm_call_ctors' */
void (*WASM_RT_ADD_PREFIX(Z___wasm_call_ctorsZ_vv))(void);
/* export: 'strcmp' */
u32 (*WASM_RT_ADD_PREFIX(Z_strcmpZ_iii))(u32, u32);
/* export: 'check_flag' */
u32 (*WASM_RT_ADD_PREFIX(Z_check_flagZ_iv))(void);
/* export: 'input' */
u32 (*WASM_RT_ADD_PREFIX(Z_inputZ_i));
/* export: 'copy_char' */
void (*WASM_RT_ADD_PREFIX(Z_copy_charZ_vii))(u32, u32);
/* export: '__dso_handle' */
u32 (*WASM_RT_ADD_PREFIX(Z___dso_handleZ_i));
/* export: '__data_end' */
u32 (*WASM_RT_ADD_PREFIX(Z___data_endZ_i));
/* export: '__global_base' */
u32 (*WASM_RT_ADD_PREFIX(Z___global_baseZ_i));
/* export: '__heap_base' */
u32 (*WASM_RT_ADD_PREFIX(Z___heap_baseZ_i));
/* export: '__memory_base' */
u32 (*WASM_RT_ADD_PREFIX(Z___memory_baseZ_i));
/* export: '__table_base' */
u32 (*WASM_RT_ADD_PREFIX(Z___table_baseZ_i));

static void init_exports(void) {
  /* export: 'memory' */
  WASM_RT_ADD_PREFIX(Z_memory) = (&w2c_memory);
  /* export: '__wasm_call_ctors' */
  WASM_RT_ADD_PREFIX(Z___wasm_call_ctorsZ_vv) = (&w2c___wasm_call_ctors);
  /* export: 'strcmp' */
  WASM_RT_ADD_PREFIX(Z_strcmpZ_iii) = (&w2c_strcmp);
  /* export: 'check_flag' */
  WASM_RT_ADD_PREFIX(Z_check_flagZ_iv) = (&w2c_check_flag);
  /* export: 'input' */
  WASM_RT_ADD_PREFIX(Z_inputZ_i) = (&w2c_input);
  /* export: 'copy_char' */
  WASM_RT_ADD_PREFIX(Z_copy_charZ_vii) = (&w2c_copy_char);
  /* export: '__dso_handle' */
  WASM_RT_ADD_PREFIX(Z___dso_handleZ_i) = (&w2c___dso_handle);
  /* export: '__data_end' */
  WASM_RT_ADD_PREFIX(Z___data_endZ_i) = (&w2c___data_end);
  /* export: '__global_base' */
  WASM_RT_ADD_PREFIX(Z___global_baseZ_i) = (&w2c___global_base);
  /* export: '__heap_base' */
  WASM_RT_ADD_PREFIX(Z___heap_baseZ_i) = (&w2c___heap_base);
  /* export: '__memory_base' */
  WASM_RT_ADD_PREFIX(Z___memory_baseZ_i) = (&w2c___memory_base);
  /* export: '__table_base' */
  WASM_RT_ADD_PREFIX(Z___table_baseZ_i) = (&w2c___table_base);
}

void WASM_RT_ADD_PREFIX(init)(void) {
  init_func_types();
  init_globals();
  init_memory();
  init_table();
  init_exports();
}
